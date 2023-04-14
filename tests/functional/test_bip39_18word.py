import pytest
from ragger.backend import SpeculosBackend
from ragger.navigator import NavInsID
from ragger.conftest import configuration

@pytest.fixture(scope='session')
def test_bip39_18word_set_seed():
    configuration.OPTIONAL.CUSTOM_SEED = "profit result tip galaxy hawk immune hockey series melody grape unusual prize nothing federal dad crew pact sad"

@pytest.mark.use_on_backend("speculos")
@pytest.mark.usefixtures('test_bip39_18word_set_seed')
def test_bip39_18word(firmware, backend, navigator):
    if firmware.device == "nanos":
        backend.wait_for_text_on_screen("Check BIP39", 5)
        backend.wait_for_text_on_screen("recovery phras", 1)
        instructions = [
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.RIGHT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.LEFT_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK,
            NavInsID.BOTH_CLICK
        ]
        navigator.navigate(instructions, screen_change_before_first_instruction=False)
        backend.wait_for_text_on_screen("BIP39 Phrase", 5)
        backend.wait_for_text_on_screen("is correct", 1)
        navigator.navigate([NavInsID.RIGHT_CLICK], screen_change_before_first_instruction=False)
        backend.wait_for_text_on_screen("Quit", 1)
        navigator.navigate([NavInsID.RIGHT_CLICK], screen_change_before_first_instruction=False)
        backend.wait_for_text_on_screen("Generate", 1)
        backend.wait_for_text_on_screen("SSKR phrases", 1)
        navigator.navigate([NavInsID.BOTH_CLICK], screen_change_before_first_instruction=False)
        backend.wait_for_text_on_screen("SSKR Share #1", 5)
        backend.wait_for_text_on_screen("tuna acid epic hard", 1)
        navigator.navigate_until_text(NavInsID.RIGHT_CLICK, [], "SSKR Share #2", 20, screen_change_before_first_instruction=False)
        backend.wait_for_text_on_screen("tuna acid epic hard", 1)
        navigator.navigate_until_text(NavInsID.RIGHT_CLICK, [], "SSKR Share #3", 20, screen_change_before_first_instruction=False)
        backend.wait_for_text_on_screen("tuna acid epic hard", 1)
        navigator.navigate_until_text(NavInsID.RIGHT_CLICK, [], "Quit", 20, screen_change_before_first_instruction=False)
