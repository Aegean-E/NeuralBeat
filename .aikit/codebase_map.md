# Codebase Map & Symbol Catalog 🗺️

> **AUTO-GENERATED & VERIFIED BY `scripts/update_knowledge_base.py`**
> This document provides an automated, up-to-date registry of all modules, classes, and exported functions across this repository.

---

## 📊 Codebase Metrics
- **Total Python Modules**: `16`
- **Total Classes**: `27`
- **Total Top-Level Functions**: `36`
- **Total Class Methods**: `131`
- **Total Source Lines**: `3802`

---

## 📦 Modules & Exported Symbols

### [`presets.py`](presets.py)
**Size**: `31` lines (`1438` bytes)

---

### [`run_tests.py`](run_tests.py)
> *NeuralBeat Test Runner*

**Size**: `46` lines (`886` bytes)

**Functions:**
- `def main()`

---

### [`SourceCode.py`](SourceCode.py)
**Size**: `1705` lines (`66408` bytes)

**Classes:**
- `class NoiseGenerator` - *Generates blocks of colored noise with state preservation using digital filters.*
  - Method `.__init__()`
  - Method `._normalize(noise)` - *Normalize noise to have RMS of 1.*
  - Method `.generate(noise_type, n_samples)`
- `class AudioConfig`
- `class BinauralGenerator` - *Generates binaural or monaural beats based on the provided AudioConfig.*
  - Method `.__init__(cfg)`
  - Method `.request_stop()` - *Signal the generator to start fading out.*
  - Method `.generate_block(frames)`
- `class IsochronicGenerator` - *Generates isochronic tones - rhythmic pulses of sound at a specific beat frequency.*
  - Method `.__init__(cfg)`
  - Method `.request_stop()`
  - Method `.generate_block(frames)`
- `class AudioEngine` - *Manages the audio playback stream using sounddevice.*
  - Method `.__init__()`
  - Method `.start(cfg)`
  - Method `.stop()` - *Stops audio gracefully with fade out.*
  - Method `.get_elapsed_time()`
  - Method `.get_last_block()`

**Functions:**
- `def load_config()` - *Loads configuration from the JSON file.*
- `def save_config(cfg)` - *Saves the configuration dictionary to the JSON file.*
- `def _normalize_category(category)`
- `def get_user_presets()`
- `def add_user_preset(category, label, left_hz, right_hz)`
- `def remove_user_preset(category, label)`
- `def get_all_presets()`
- `def clamp(value, lo, hi)` - *Clamps a value between lo and hi.*
- `def validate_audio_params(freq_l, freq_r, vol_l, vol_r, duration)` - *Validates audio parameters (frequencies, volumes, duration).*
- `def _compute_ramped_beat_hz(elapsed_s, start_beat_hz, end_beat_hz, ramp_s)` - *Calculates the current beat frequency based on ramp progress.*
- `def get_audio_config_from_ui()` - *Reads values from UI entries and returns an AudioConfig object.*
- `def stop_audio()`
- `def set_osc_merge_waves()` - *Saves the merge waves setting and updates the live plot's static elements.*
- `def set_osc_colors(palette_name)` - *Sets the oscilloscope color palette and saves to config.*
- `def toggle_oscilloscope_window()` - *Opens or closes the real-time oscilloscope window.*
- `def _run_export_thread(cfg, filename, duration, progress_win, progress_bar, progress_label, on_success, on_error)` - *Background thread function for exporting audio to a WAV file.*
- `def export_audio_file()` - *Initiates the audio export process with UI dialogs.*
- `def play_audio()` - *Starts audio playback based on current UI settings.*
- `def show_about()`
- `def set_theme(theme_name)`
- `def export_config_json()` - *Export the current in-memory config dict to a JSON file the user selects.*
- `def import_config_json()` - *Import config from a JSON file, persist it, and refresh UI (theme + presets).*
- `def apply_preset(left_hz, right_hz, category, carrier_hz, pulse_hz)`
- `def build_preset_buttons()`
- `def save_current_as_preset()`
- `def delete_preset()`
- `def update_live_status()` - *Updates the status bar with current frequencies and remaining time.*
- `def on_close()`
- `def create_frequency_control_frame(parent, title, column, waveform_options, default_freq, default_vol, default_waveform)`
- `def main()` - *Main application entry point. Initializes UI and starts the event loop.*

---

### [`tests/__init__.py`](tests/__init__.py)
**Size**: `0` lines (`0` bytes)

---

### [`tests/test_audio_config.py`](tests/test_audio_config.py)
> *Test AudioConfig dataclass and utility functions.*

**Size**: `216` lines (`6612` bytes)

**Classes:**
- `class TestAudioConfig` - *Test AudioConfig dataclass.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_audio_config_defaults()` - *Test AudioConfig default values.*
  - Method `.test_audio_config_isochronic()` - *Test AudioConfig with isochronic beat type.*
- `class TestClampFunction` - *Test clamp utility function.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_clamp_basic()` - *Test basic clamping.*
  - Method `.test_clamp_edge_cases()` - *Test clamp edge cases.*
- `class TestRampCalculation` - *Test ramp computation function.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_ramp_no_ramp()` - *Test ramp calculation when ramp is disabled (returns end_beat_hz).*
  - Method `.test_ramp_linear()` - *Test linear ramp calculation.*
  - Method `.test_ramp_at_end()` - *Test ramp at end point.*
  - Method `.test_ramp_beyond_end()` - *Test ramp beyond duration.*
- `class TestValidation` - *Test validation functions.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_validate_valid_params()` - *Test validation with valid parameters.*
  - Method `.test_validate_invalid_left_freq()` - *Test validation with invalid left frequency.*
  - Method `.test_validate_invalid_volume()` - *Test validation with invalid volume.*

---

### [`tests/test_audio_engine.py`](tests/test_audio_engine.py)
> *Test the AudioEngine class from SourceCode.py.*

**Size**: `131` lines (`4140` bytes)

**Classes:**
- `class TestAudioEngine` - *Test the AudioEngine class.*
  - Method `.test_start_binaural(mock_binaural_gen, mock_sd)` - *Test starting the audio engine for binaural beats.*
  - Method `.test_start_isochronic(mock_isochronic_gen, mock_sd)` - *Test starting the audio engine for isochronic tones.*
  - Method `.test_stop(mock_binaural_gen, mock_sd)` - *Test stopping the audio engine.*
  - Method `.test_stop_when_not_playing(mock_sd)` - *Test that stop() does nothing if not playing.*
  - Method `.test_start_exception(mock_logger, mock_sd)` - *Test exception handling during start.*
  - Method `.test_get_elapsed_time()` - *Test elapsed time calculation.*

---

### [`tests/test_bootstyle_usage.py`](tests/test_bootstyle_usage.py)
> *Regression shield: ttkbootstrap-only keyword arguments must stay on ttkbootstrap widgets.*

**Size**: `51` lines (`1835` bytes)

**Classes:**
- `class TestBootstyleUsage`
  - Method `.test_bootstyle_only_on_ttkbootstrap_widgets()`

**Functions:**
- `def find_bootstyle_violations(source)`

---

### [`tests/test_config.py`](tests/test_config.py)
> *Test configuration management functions.*

**Size**: `190` lines (`7040` bytes)

**Classes:**
- `class TestConfig` - *Test configuration management functions.*
  - Method `.setUp()` - *Patch the config object for each test.*
  - Method `.tearDown()`
  - Method `.test_normalize_category()` - *Test _normalize_category function.*
  - Method `.test_get_user_presets_empty()` - *Test get_user_presets with an empty config.*
  - Method `.test_get_user_presets_populated()` - *Test get_user_presets with a populated config.*
  - Method `.test_add_user_preset()` - *Test adding a new user preset.*
  - Method `.test_add_user_preset_invalid_values()` - *Test adding a preset with invalid numeric values.*
  - Method `.test_add_user_preset_empty_label()` - *Test adding a preset with an empty label.*
  - Method `.test_remove_user_preset()` - *Test removing an existing user preset.*
  - Method `.test_remove_user_preset_not_found()` - *Test removing a preset that does not exist.*
  - Method `.test_save_config(mock_path)` - *Test the actual save_config function.*
  - Method `.test_load_config_exists(mock_path)` - *Test loading an existing config file.*
  - Method `.test_load_config_not_exists(mock_path)` - *Test loading when config file does not exist.*
  - Method `.test_load_config_error(mock_logger, mock_path)` - *Test loading a corrupt config file.*

---

### [`tests/test_config_presets.py`](tests/test_config_presets.py)
> *Test config and preset management functions.*

**Size**: `267` lines (`8956` bytes)

**Classes:**
- `class TestNormalizeCategory` - *Test _normalize_category function.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_normalize_binaural()` - *Test normalization of binaural.*
  - Method `.test_normalize_monaural()` - *Test normalization maps monaural to Binaural.*
  - Method `.test_normalize_isochronic()` - *Test normalization of isochronic.*
  - Method `.test_normalize_invalid()` - *Test invalid category raises ValueError.*
- `class TestGetUserPresets` - *Test get_user_presets function.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_get_user_presets_empty()` - *Test get_user_presets with no config file.*
  - Method `.test_get_user_presets_with_data()` - *Test get_user_presets with user presets.*
- `class TestGetAllPresets` - *Test get_all_presets function.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_get_all_presets_structure()` - *Test get_all_presets returns correct keys.*
  - Method `.test_get_all_presets_includes_defaults()` - *Test get_all_presets includes default presets.*
  - Method `.test_get_all_presets_merges_user()` - *Test get_all_presets merges user presets.*
- `class TestAddUserPreset` - *Test add_user_preset function.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_add_user_preset_isochronic()` - *Test adding isochronic preset.*
  - Method `.test_add_user_preset_binaural()` - *Test adding binaural preset.*
- `class TestRemoveUserPreset` - *Test remove_user_preset function.*
  - Method `.setUpClass()`
  - Method `.tearDownClass()`
  - Method `.test_remove_existing_preset()` - *Test removing existing preset returns True.*
  - Method `.test_remove_nonexistent_preset()` - *Test removing nonexistent preset returns False.*

---

### [`tests/test_dsp_generators.py`](tests/test_dsp_generators.py)
> *Test the DSP generator classes (BinauralGenerator, IsochronicGenerator).*

**Size**: `186` lines (`6924` bytes)

**Classes:**
- `class TestBinauralGenerator` - *Tests for the BinauralGenerator class.*
  - Method `.setUp()` - *Set up a default AudioConfig for tests.*
  - Method `.test_block_generation()` - *Test that a block of audio is generated with the correct shape and type.*
  - Method `.test_fade_in()` - *Test that the signal fades in at the beginning.*
  - Method `.test_fade_out()` - *Test that the signal fades out and finishes when stop is requested.*
  - Method `.test_noise_mixing()` - *Test that noise is correctly added to the signal.*
  - Method `.test_ramp_mode()` - *Test that ramp mode runs without error and produces output.*
- `class TestIsochronicGenerator` - *Tests for the IsochronicGenerator class.*
  - Method `.setUp()` - *Set up a default AudioConfig for tests.*
  - Method `.test_block_generation()` - *Test that a block of isochronic tones is generated correctly.*

---

### [`tests/test_generators.py`](tests/test_generators.py)
> *Test generator classes.*

**Size**: `267` lines (`7901` bytes)

**Classes:**
- `class TestBinauralGenerator` - *Test BinauralGenerator class.*
  - Method `.setUpClass()`
  - Method `.test_generator_initialization()` - *Test BinauralGenerator initializes correctly.*
  - Method `.test_generator_creates_output()` - *Test BinauralGenerator creates audio output.*
  - Method `.test_generator_fade_in()` - *Test fade-in at start.*
  - Method `.test_request_stop()` - *Test request_stop sets stopping flag.*
- `class TestMonauralGenerator` - *Test MonauralGenerator class.*
  - Method `.setUpClass()`
  - Method `.test_generator_initialization()` - *Test MonauralGenerator initializes correctly.*
  - Method `.test_generator_creates_output()` - *Test MonauralGenerator creates audio output.*
- `class TestIsochronicGenerator` - *Test IsochronicGenerator class.*
  - Method `.setUpClass()`
  - Method `.test_generator_initialization()` - *Test IsochronicGenerator initializes correctly.*
  - Method `.test_generator_creates_output()` - *Test IsochronicGenerator creates audio output.*
  - Method `.test_generator_pulse_modulation()` - *Test IsochronicGenerator has pulsing.*
  - Method `.test_request_stop()` - *Test request_stop sets stopping flag.*
- `class TestGeneratorWaveforms` - *Test generator with different waveforms.*
  - Method `.setUpClass()`
  - Method `.test_generator_with_sine()` - *Test generator with Sine waveform.*
  - Method `.test_generator_with_ramp()` - *Test generator with ramp enabled.*

**Functions:**
- `def create_numpy_mock()` - *Create a more complete numpy mock.*

---

### [`tests/test_presets.py`](tests/test_presets.py)
> *Test presets module.*

**Size**: `69` lines (`2733` bytes)

**Classes:**
- `class TestPresets` - *Test preset data structures.*
  - Method `.test_monaural_presets_structure()` - *Test monaural presets have required fields.*
  - Method `.test_binaural_presets_structure()` - *Test binaural presets have required fields.*
  - Method `.test_isochronic_presets_structure()` - *Test isochronic presets have required fields.*
  - Method `.test_brainwave_ranges()` - *Test brainwave ranges are defined.*
  - Method `.test_frequency_ranges_valid()` - *Test brainwave frequency ranges are valid.*
  - Method `.test_presets_not_empty()` - *Test all preset lists are populated.*

---

### [`tests/test_ui_logic.py`](tests/test_ui_logic.py)
> *Test UI logic functions from SourceCode.py that don't require a live UI.*

**Size**: `240` lines (`10044` bytes)

**Classes:**
- `class TestUiLogic` - *Test UI-related logic functions.*
  - Method `.test_get_audio_config_manual_mode(*mocks)` - *Test get_audio_config_from_ui in manual mode.*
  - Method `.test_get_audio_config_ramp_mode(*mocks)` - *Test get_audio_config_from_ui in ramp mode.*
  - Method `.test_get_audio_config_invalid_input(*mocks)` - *Test get_audio_config_from_ui with invalid text input.*
  - Method `.test_get_audio_config_out_of_range(*mocks)` - *Test get_audio_config_from_ui with out-of-range frequency.*
  - Method `.test_build_preset_buttons(mock_apply_preset)` - *Test that preset buttons are created with the correct commands.*
  - Method `.test_apply_preset()` - *Test that apply_preset correctly updates the UI entries.*

**Functions:**
- `def patch_ui_globals(func)` - *Patch every UI global and pass the mocks in the order the tests unpack them.*

---

### [`tests/test_utils.py`](tests/test_utils.py)
> *Test utility functions from SourceCode.py.*

**Size**: `108` lines (`4132` bytes)

**Classes:**
- `class TestUtils` - *Test utility functions.*
  - Method `.test_clamp()` - *Test the clamp function.*
  - Method `.test_validate_audio_params_valid()` - *Test validate_audio_params with valid inputs.*
  - Method `.test_validate_audio_params_invalid_freq()` - *Test validate_audio_params with invalid frequencies.*
  - Method `.test_validate_audio_params_invalid_vol()` - *Test validate_audio_params with invalid volumes.*
  - Method `.test_validate_audio_params_invalid_duration()` - *Test validate_audio_params with invalid duration.*
  - Method `.test_compute_ramped_beat_hz()` - *Test _compute_ramped_beat_hz calculation.*

---

### [`tests/verify_dsp_ramp.py`](tests/verify_dsp_ramp.py)
**Size**: `122` lines (`4030` bytes)

**Classes:**
- `class FakeNumpy`
  - Method `.arange(*args, **kwargs)`
  - Method `.sin(x)`
  - Method `.tanh(x)`
  - Method `.clip(a, a_min, a_max)`
  - Method `.column_stack(tup)`
  - Method `.full(shape, fill_value, **kwargs)`
  - Method `.maximum(x1, x2)`
  - Method `.cumsum(a)`
  - Method `.concatenate(tup)`
  - Method `.sum(a)`
  - Method `.abs(a)`
  - Method `.max(a)`

---

### [`verification.py`](verification.py)
**Size**: `173` lines (`6480` bytes)

**Functions:**
- `def validate_signal(audio_data, sample_rate, expected_left_hz, expected_right_hz, duration_s, tolerance_hz)` - *Validates the generated audio signal for scientific accuracy.*
- `def validate_export(generator_class, config, duration_s)` - *Validates that the exported WAV file matches the in-memory generation.*

---
