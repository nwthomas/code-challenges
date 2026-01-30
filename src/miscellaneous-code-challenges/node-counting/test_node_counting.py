from node_counting import AsyncMachineNode
import pytest


@pytest.mark.asyncio
async def test_async_machine_node_small_tree(capsys):
    child1 = AsyncMachineNode()
    child2 = AsyncMachineNode()
    root = AsyncMachineNode([child1, child2])

    await root.count_machines()

    captured = capsys.readouterr()
    assert "Total machines in tree: 3" in captured.out


@pytest.mark.asyncio
async def test_async_machine_node_large_tree(capsys):
    root = AsyncMachineNode(
        [
            AsyncMachineNode(
                [
                    AsyncMachineNode([AsyncMachineNode() for _ in range(10)])
                    for _ in range(10)
                ]
            )
            for _ in range(10)
        ]
    )
    await root.count_machines()

    captured = capsys.readouterr()
    assert "Total machines in tree: 1001" in captured.out
