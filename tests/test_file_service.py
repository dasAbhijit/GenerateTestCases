import pytest
from pathlib import Path
from generate_test_cases.utils.file_service import FileService

@pytest.fixture
def file_service():
    return FileService()

@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    return file_path

def test_read_file(file_service, test_file):
    content = file_service.read_file(test_file)
    assert content == "test content"

def test_read_file_not_found(file_service):
    with pytest.raises(FileNotFoundError):
        file_service.read_file(Path("nonexistent.txt"))

def test_save_to_csv(file_service, tmp_path):
    data = "header1,header2\nvalue1,value2"
    output_path = tmp_path / "test.csv"
    
    result = file_service.save_to_csv(data, output_path)
    
    assert result == output_path
    assert output_path.exists()
    content = output_path.read_text()
    assert "header1,header2" in content
    assert "value1,value2" in content

def test_save_to_csv_with_markers(file_service, tmp_path):
    data = "```csv\nheader1,header2\nvalue1,value2\n```"
    output_path = tmp_path / "test.csv"
    
    result = file_service.save_to_csv(data, output_path)
    
    assert result == output_path
    assert output_path.exists()
    content = output_path.read_text()
    assert "```csv" not in content
    assert "```" not in content
    assert "header1,header2" in content
    assert "value1,value2" in content 