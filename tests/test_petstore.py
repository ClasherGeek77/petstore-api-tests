import pytest
from flaky import flaky
from utils.api_helper import create_pet, get_pet_by_id, find_pets_by_status

@flaky(max_runs=5, min_passes=1)
@pytest.mark.parametrize("pet_name", ["Cat1", "Cat2"])
def test_add_new_pet(pet_name):
    status_code, pet = create_pet(pet_name)
    assert status_code == 200, f"status: {status_code}, response: {pet}"
    assert pet["name"] == pet_name


def test_find_by_status_available():
    status_code, pets = find_pets_by_status("available")
    assert status_code == 200
    assert all(p["status"] == "available" for p in pets)

def test_find_by_status_pending():
    status_code, pets = find_pets_by_status("pending")
    assert status_code == 200
    assert all(p["status"] == "pending" for p in pets)

def test_get_existing_pet():
    status_code, pet = get_pet_by_id(2)
    assert status_code == 200
    assert "id" in pet

