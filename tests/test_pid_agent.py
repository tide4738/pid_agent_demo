import numpy as np
from pid_agent_sim import IndustrialPlant, PIDAgent


def test_plant_update():
    p = IndustrialPlant(dt=0.1)
    initial = p.process_value
    pv = p.update(0.5)
    assert isinstance(pv, float)
    assert p.process_value != initial or p.velocity != 0


def test_pid_agent_run_simulation():
    agent = PIDAgent()
    history = agent.run_simulation(target=1.0, steps=10)
    assert hasattr(history, '__len__')
    assert len(history) == 10
    assert np.all(np.isfinite(history))
