from pathlib import Path
import pytest

import spike2py_preprocess.utils as utils
import spike2py_reflex as s2pr
import spike2py as s2p


DATA = Path(__file__).parent / "data"
STUDY1_PATH = Path(__file__).parent / "data" / 'study1'


@pytest.fixture()
def study1_path():
    return STUDY1_PATH

@pytest.fixture()
def sub01_proc_path():
    return STUDY1_PATH / 'sub01'

@pytest.fixture()
def sub01_proc_path():
    return STUDY1_PATH / 'sub01' / 'proc' / 'biphasic_high_fq_mmax_reflex.json'


@pytest.fixture()
def demo_study_reflex():
    return utils.read_json(DATA / "demo_study_reflex.json")


@pytest.fixture()
def demo_subject_windows_long():
    return {
        "sd": [-50, -20],
        "extract": {
            "single": [
                -100,
                100
            ],
            "double": [
                -250,
                150
            ],
            "double_single_pulse": [
                -15,
                40
            ],
            "train_single_pulse": [
                -15,
                30
            ]
        },
        "plotting": {
            "single": [
                -25,
                50
            ],
            "double": [
                -25,
                75
            ],
            "double_single_pulse": [
                -15,
                40
            ],
            "train_single_pulse": [
                -15,
                30
            ]
        },
        "reflexes": {
            "Fdi": {
                "mmax": [
                    8,
                    15
                ],
                "hreflex": [
                    12,
                    35
                ]
            }
        }
    }


@pytest.fixture()
def demo_subject_windows_short():
    return {
        "sd": [-51, -21],
        "reflexes": {
            "Fdi": {
        "mmax": {
          "mmax": [
            6,
            21
          ],
          "hreflex": [
            26,
            45
          ]
        },
        "hreflex": {
          "hreflex": [
            21,
            48
          ]
        },
        "ramp": {
          "cool_reflex": [
            6,
            24
          ]
        }
        }
    }
    }


@pytest.fixture()
def demo_section_windows_short():
    return {
        "sd": [-58, -26],
        "reflexes": {
            "Fdi": {
                "mmax": {
                    "mmax": [
                        8,
                        26
                    ],
                    "hreflex": [
                        19,
                        39
                    ]
                },
                "hreflex": {
                    "hreflex": [
                        25,
                        44
                    ]
                },
                "ramp": {
                    "cool_reflex": [
                        7,
                        33
                    ]
                }
            }
        }
    }


@pytest.fixture()
def subject_channels():
    return {'emg': ['MG'],
            'triggers':
                {'mmax': {'channels': 'Mmax', 'type': 'single'},
                 'ramp': {'channels': 'Ds8', 'type': 'single'},
                 'hreflex': {'channels': 'Ds8', 'type': 'double'}},
            'stim_intensity': 'zap'}


@pytest.fixture()
def section_channels():
    return {'emg': ['hh'],
            'triggers':
                {'Mmax': {'channels': 'trig1', 'type': 'double'},
                 'rRamp': {'channels': 'trig2', 'type': 'single'},
                 'H_reflex': {'channels': 'trig3', 'type': 'double'}},
            'stim_intensity': 'zapzap'}


@pytest.fixture()
def info_data_hreflex():
    info = s2pr.info.Info(STUDY1_PATH)
    info.init_subject('sub01')
    info.trial = 'biphasic_high_fq'
    section_name = 'hreflex'
    info.init_section(section_name)
    data = s2p.trial.load(info.section_pkl)
    info.triggers = s2pr.utils.Triggers(info, data)
    return info, data


@pytest.fixture()
def info_data_mmax():
    info = s2pr.info.Info(STUDY1_PATH)
    info.init_subject('sub01')
    info.trial = 'biphasic_high_fq'
    section_name = 'mmax'
    info.init_section(section_name)
    data = s2p.trial.load(info.section_pkl)
    info.triggers = s2pr.utils.Triggers(info, data)
    return info, data


@pytest.fixture()
def info_data_ramp():
    info = s2pr.info.Info(STUDY1_PATH)
    info.init_subject('sub01')
    info.trial = 'biphasic_high_fq'
    section_name = 'ramp'
    info.init_section(section_name)
    data = s2p.trial.load(info.section_pkl)
    info.triggers = s2pr.utils.Triggers(info, data)
    return info, data