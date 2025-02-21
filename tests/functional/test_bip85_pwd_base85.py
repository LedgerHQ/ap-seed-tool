from pytest import fixture
from pytest import mark
from pytest import skip
from ragger.navigator import NavInsID
from ragger.conftest import configuration

@fixture(scope='session')
def set_seed():
    # Seed taken from https://github.com/bitcoin/bips/blob/master/bip-0085.mediawiki
    configuration.OPTIONAL.CUSTOM_SEED = "install scatter logic circle pencil average fall shoe quantum disease suspect usage"

def stax_bip85_pwd_base85(backend):
    backend.wait_for_text_on_screen("Seed Tool", 10)
    backend.finger_touch(106, 510, 1)
    backend.wait_for_text_on_screen("BIP85 Generate", 5)
    backend.finger_touch(124, 430, 1)
    backend.wait_for_text_on_screen("Which BIP85", 5)
    backend.finger_touch(124, 430, 1)
    backend.wait_for_text_on_screen("Enter password length", 5)
    backend.finger_touch(50, 300, 1)  # 1
    backend.finger_touch(195, 300, 1) # 2
    backend.finger_touch(340, 600, 1)
    backend.wait_for_text_on_screen("Enter index", 5)
    backend.finger_touch(195, 600, 1) # 0
    backend.finger_touch(340, 600, 1)
    backend.wait_for_text_on_screen(r"_s`{TW89\)i4`", 1)
    backend.finger_touch(80, 630, 1)
    backend.wait_for_text_on_screen("Seed Tool", 5)
    backend.finger_touch(200, 630, 1)

def flex_bip85_pwd_base85(backend):
    backend.wait_for_text_on_screen("Seed Tool", 10)
    backend.finger_touch(240, 440, 1)
    backend.wait_for_text_on_screen("BIP85 Generate", 5)
    backend.finger_touch(240, 320, 1)
    backend.wait_for_text_on_screen("Which BIP85", 5)
    backend.finger_touch(240, 330, 1)
    backend.wait_for_text_on_screen("Enter password length", 5)
    backend.finger_touch(50, 300, 1) #  1
    backend.finger_touch(195, 300, 1) # 2
    backend.finger_touch(400, 560, 1)
    backend.wait_for_text_on_screen("Enter index", 5)
    backend.finger_touch(240, 560, 1) # 0
    backend.finger_touch(400, 560, 1)
    backend.wait_for_text_on_screen(r"_s`{TW89\)i4`", 1)
    backend.finger_touch(100, 550, 1)
    backend.wait_for_text_on_screen("Seed Tool", 5)
    backend.finger_touch(240, 550, 1)

@mark.use_on_backend("speculos")
def test_bip85_pwd_base85(firmware, backend, navigator, set_seed):
    if firmware.device == "nanos":
        skip("Skipping test for Nano S device")
    elif firmware.device == "nanosp":
        skip("Skipping test for Nano S+ device")
    elif firmware.device == "nanox":
        skip("Skipping test for Nano X device")
    elif firmware.device == "stax":
        stax_bip85_pwd_base85(backend)
    elif firmware.device == "flex":
        flex_bip85_pwd_base85(backend)
