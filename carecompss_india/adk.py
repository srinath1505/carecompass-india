# adk.py — Lightweight mock of Google ADK for local development

class Memory:
    def __init__(self):
        self._store = {}

    def set(self, key, value):
        self._store[key] = value

    def get(self, key, default=None):
        return self._store.get(key, default)

# Global memory instance (as in ADK)
memory = Memory()

def Tool(func):
    """Decorator to mark a function as a tool"""
    func.is_tool = True
    return func

def Agent(name: str, instructions: str, tools: list = None):
    """Mock Agent factory that returns a callable agent object"""
    class MockAgent:
        def __init__(self, name, instructions, tools):
            self.name = name
            self.instructions = instructions
            self.tools = tools or []

        def chat(self, message: str) -> str:
            # In a real ADK, this would invoke planning/tool calling
            # Here, we simulate the coordinator logic directly
            from main import simulate_coordinator_response
            return simulate_coordinator_response(message)

    return MockAgent(name, instructions, tools)