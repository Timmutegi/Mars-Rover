import pytest
from MarsRover import MarsRover

top_right_coordinates = {
    "x": 5,
    "y": 5
}

mars_rover = MarsRover(top_right_coordinates)

def test_deploy_rover_failed():
    with pytest.raises(Exception):
        mars_rover.deploy_rover(-1, -1, "N", "LMLMLMLMM")

def test_deploy_rover_successful():
    final_position = mars_rover.deploy_rover(1, 2, "N", "LMLMLMLMM")
    assert final_position == {
        'x': 1,
        'y': 3,
        'orientation': "N"
    }
