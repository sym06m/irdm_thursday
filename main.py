class StarterAgent:
    def __init__(self, name):
        self.name = name

    def run(self, prompt):
        return f"{self.name} response: {prompt}"

if __name__ == "__main__":
    agent = StarterAgent("StarterPackAgent")
    print(agent.run("Hello from Agent Starter Pack"))
