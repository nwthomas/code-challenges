"""
You are given a tree, where each node represents a machine.

Communication is only possible between parent and child nodes.
The communication relies on the provided interfaces:
- sendAsyncMessage(target, message): Sends an asynchronous message (already implemented, no need to implement).
- receiveMessage(message): A method you need to implement for handling incoming messages.

Question 1: Count the total number of machines
Goal: Design a method to count how many machines exist in the entire tree.

Basic logic:
When receiveMessage(message) receives a count message, it forwards the same message to all of its children.
When it receives a response message from a child, it records the child’s count.
Once all child responses are collected, it computes the sum and sends the result back to its parent.

Special cases:
If the node is a leaf (no children), it directly returns 1 to its parent.
If the node is the root, the final sum is the total number of machines in the tree.

Example:
A 3-level tree: root → 2 children → each child has 2 leaves.
The result should be 7 machines in total.

Key Points:
Distributed communication model: Only parent-child message passing is allowed.
Recursive counting logic: count request propagates down → responses bubble up → aggregate results.
Boundary conditions: Special handling for root and leaf nodes.
Robustness: Must handle potential failures (e.g., lost messages, missing child responses).
"""

from typing import Any, Dict, Optional
import uuid
import asyncio


class AsyncMachineNode:
    def __init__(self, children=None):
        self.children: list["AsyncMachineNode"] = children or []
        self.requests: Dict[str, Dict[str, Any]] = {}

    async def sendAsyncMessage(self, target: "AsyncMachineNode", message: str) -> None:
        """Sends an sync message. This is prepared for us normally as a network call but implemented here for testing."""
        await target.receiveMessage(message)

    async def receiveMessage(self, message: Dict[str, Any]) -> None:
        msg_type: str = message["type"]
        request_id: str = message["request_id"]

        if msg_type == "COUNT_REQUEST":
            parent: Optional["AsyncMachineNode"] = message.get("parent")
            num_children: int = len(self.children)

            if num_children == 0:
                if parent:
                    await self.sendAsyncMessage(
                        parent,
                        {
                            "type": "COUNT_RESPONSE",
                            "request_id": request_id,
                            "count": 1,
                        },
                    )
                else:
                    print(f"Total machines in tree: 1")
            else:
                future: asyncio.Future[int] = asyncio.Future()
                self.requests[request_id] = {
                    "responses_expected": num_children,
                    "responses_received": 0,
                    "child_count_sum": 0,
                    "parent": parent,
                    "future": future,
                }

                for child in self.children:
                    await self.sendAsyncMessage(
                        child,
                        {
                            "type": "COUNT_REQUEST",
                            "request_id": request_id,
                            "parent": self,
                        },
                    )

                await future

        elif msg_type == "COUNT_RESPONSE":
            count: int = message["count"]
            state = self.requests[request_id]

            state["child_count_sum"] += count
            state["responses_received"] += 1

            if state["responses_received"] == state["responses_expected"]:
                total_count: int = state["child_count_sum"]
                if state["parent"] is None:
                    total_count += 1

                parent: Optional["AsyncMachineNode"] = state["parent"]

                if parent:
                    await self.sendAsyncMessage(
                        parent,
                        {
                            "type": "COUNT_RESPONSE",
                            "request_id": request_id,
                            "count": total_count,
                        },
                    )
                else:
                    print(f"Total machines in tree: {total_count}")

                future: asyncio.Future[int] = state["future"]
                if not future.done():
                    future.set_result(total_count)

                del self.requests[request_id]

    async def count_machines(self) -> None:
        """Counts number of nodes from current node downward in tree."""
        request_id = str(uuid.uuid4())
        await self.receiveMessage(
            {
                "type": "COUNT_REQUEST",
                "request_id": request_id,
                "parent": None,
            }
        )
