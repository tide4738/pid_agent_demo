import numpy as np
import matplotlib.pyplot as plt

class IndustrialPlant:
    """A simple industrial process model."""
    def __init__(self, dt=0.1):
        self.dt = dt
        self.process_value = 0.0
        self.velocity = 0.0
        self.inertia = 0.8  # inertia
        self.damping = 0.1  # damping

    def update(self, control_input):
        # Simple second-order system simulation.
        acceleration = control_input - self.damping * self.velocity
        self.velocity += acceleration * self.dt
        self.process_value += self.velocity * self.dt
        return self.process_value

class PIDAgent:
    """A closed-loop agent that tunes PID gains."""
    def __init__(self):
        self.kp = 0.1
        self.ki = 0.01
        self.kd = 0.01

    def run_simulation(self, target=10.0, steps=100):
        plant = IndustrialPlant()
        pv_history = []
        integral = 0
        last_error = 0
        
        for _ in range(steps):
            error = target - plant.process_value
            integral += error
            derivative = error - last_error
            u = self.kp * error + self.ki * integral + self.kd * derivative
            pv = plant.update(u)
            pv_history.append(pv)
            last_error = error
        return np.array(pv_history)

    def evaluate(self, history, target=10.0):
        # Review metrics: overshoot and average error over the last 10 steps.
        overshoot = np.max(history) - target
        final_error = np.abs(np.mean(history[-10:]) - target)
        return overshoot, final_error

    def self_optimize(self, target=10.0):
        print("Agent started: running generate-evaluate-feedback loop...")
        best_error = float('inf')
        
        # Simulate three optimization rounds.
        for i in range(1, 4):
            history = self.run_simulation(target)
            overshoot, final_error = self.evaluate(history, target)
            print(f"Round {i} evaluation: overshoot={overshoot:.2f}, steady-state error={final_error:.2f}")
            
            if final_error < 0.1 and overshoot < 0.5:
                print("Strategy passed evaluation, using final control logic.")
                break
            else:
                print("Metrics not met; adjusting gains and trying again...")
                # Simulate parameter adjustment.
                self.kp += 0.5
                self.ki += 0.05
                self.kd += 0.2
        return history

# Demo run.
if __name__ == "__main__":
    agent = PIDAgent()
    
    # Initial run before optimization.
    bad_history = agent.run_simulation()
    
    # Run the agent optimization loop.
    optimized_history = agent.self_optimize()

    # Visualize results.
    plt.figure(figsize=(10, 5))
    plt.plot(bad_history, label='Initial (Unoptimized)', linestyle='--')
    plt.plot(optimized_history, label='Agent Optimized', linewidth=2)
    plt.axhline(y=10, color='r', linestyle=':', label='Target')
    plt.title("Industrial Control Optimization: AI Agent vs Manual")
    plt.xlabel("Time Steps")
    plt.ylabel("Process Value")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Simulation complete, results generated.")