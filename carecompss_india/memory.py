# memory.py
from adk import Memory

# Global memory instance
memory = Memory()

# Helper functions for agent result storage
def store_result(agent_name: str, data: str):
    """Store result from an agent in shared memory"""
    memory.set(f"{agent_name}_result", data)

def get_result(agent_name: str) -> str:
    """Retrieve result from an agent"""
    return memory.get(f"{agent_name}_result", "No data available")