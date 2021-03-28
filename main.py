import itertools
import datetime
import sys

from spirecomm.communication.coordinator import Coordinator
from spirecomm.ai.agent import SimpleAgent
from spirecomm.spire.character import PlayerClass


if __name__ == "__main__":
    log = 'spirecomm_log.txt'
    agent = SimpleAgent()
    coordinator = Coordinator(log)
    coordinator.signal_ready()
    coordinator.register_command_error_callback(agent.handle_error)
    coordinator.register_state_change_callback(agent.get_next_action_in_game)
    coordinator.register_out_of_game_callback(agent.get_next_action_out_of_game)

    # Play games forever, cycling through the various classes
    for chosen_class in itertools.cycle(PlayerClass):
        agent.change_class(chosen_class)
        result = coordinator.play_one_game(chosen_class)
