class AgentEngine:
    def deploy(self, agent_name):
        return f"Agent '{agent_name}' deployed successfully."

if __name__ == "__main__":
    engine = AgentEngine()
    print(engine.deploy("starter_pack_agent"))
