import pytest
from io import StringIO
from heap_stacks.heap_food_orders import main


@pytest.fixture
def load_test_data():
    # Load input and expected output from files
    with open("test_input_2.txt", "r") as input_file, open("test_output_2.txt", "r") as output_file:
        test_input = input_file.read()
        expected_output = output_file.read()
    return test_input, expected_output


def test_customer_service(monkeypatch, capsys, load_test_data):
    # Load the input and expected output
    test_input, expected_output = load_test_data

    # Simulate the input
    monkeypatch.setattr('sys.stdin', StringIO(test_input))

    # Run the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Assert the output matches the expected output
    assert captured.out.strip() == expected_output.strip()
