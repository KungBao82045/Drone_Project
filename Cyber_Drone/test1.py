import asyncio

active = asyncio.Event()

async def test1():
    if not active.is_set() and h_voice[-1] == "start":
        active.set()
        print("Test start")
        try:
            await asyncio.sleep(15)  # Simulating a long-running task
        except asyncio.CancelledError:
            print("Task was cancelled!")  # Handle cancellation
        finally:
            print("TestDone")
            active.clear()

# Running and cancelling the task
async def main():
    global h_voice
    h_voice = ["start"]  # Simulating external voice command

    task = asyncio.create_task(test1())  # Start test1 as a task
    await asyncio.sleep(5)  # Let it run for 5 seconds
    task.cancel()  # Cancel the task
    await asyncio.sleep(1)  # Give time for cleanup
    print("Main Done")

asyncio.run(main())
