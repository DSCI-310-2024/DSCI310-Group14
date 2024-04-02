import os
import pytest
import tempfile
import pandas as pd
import numpy as np
from click.testing import CliRunner
from scripts.eda import main

def generate_dummy_data():
    """Generate a dummy dataset for testing."""
    data = {
        'Access to electricity (% of population)': np.random.rand(10) * 100,
        'CO2 emissions (kt)': np.random.rand(10) * 1000,
        'Population, total': np.random.randint(100000, 1000000, size=10),
        'Renewable energy consumption (% of total final energy consumption)': np.random.rand(10) * 100,
        'Land area (sq. km)': np.random.rand(10) * 1000,
        'Death rate, crude (per 1,000 people)': np.random.rand(10) * 10,
        'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)': np.random.rand(10) * 50,
        'Adjusted net national income (constant 2015 US$)': np.random.rand(10) * 1e6,
        'Renewable electricity output (% of total electricity output)': np.random.rand(10) * 100
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def dummy_data_file():
    """Create a dummy data CSV file."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.csv') as tmpfile:
        df = generate_dummy_data()
        df.to_csv(tmpfile.name, index=False)
        return tmpfile.name

def test_eda_output_file(dummy_data_file):
    """Test that the EDA script creates an output file."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        output_path = 'eda_output.png'
        result = runner.invoke(main, ['--data_path', dummy_data_file, '--output_path', output_path])
        assert result.exit_code == 0
        assert os.path.exists(output_path)
        assert 'EDA figure saved' in result.output

def test_eda_output_content(dummy_data_file):
    """Test to ensure the output file is not empty (optional, requires matplotlib image comparison or file size check)."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        output_path = 'eda_output.png'
        runner.invoke(main, ['--data_path', dummy_data_file, '--output_path', output_path])
        assert os.path.getsize(output_path) > 0, "Output file is empty or missing"
