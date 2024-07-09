import struct

# Mapping of key codes to characters without shift
KEY_MAP = {
    0x02: '&', 0x03: 'é', 0x04: '"', 0x05: "'", 0x06: '(', 0x07: '§', 0x08: 'è', 0x09: '!', 0x0A: 'ç', 0x0B: 'à',
    0x0C: ')', 0x0D: '=', 0x10: 'a', 0x11: 'z', 0x12: 'e', 0x13: 'r', 0x14: 't', 0x15: 'y', 0x16: 'u', 0x17: 'i',
    0x18: 'o', 0x19: 'p', 0x1A: '^', 0x1B: '$', 0x1E: 'q', 0x1F: 's', 0x20: 'd', 0x21: 'f', 0x22: 'g', 0x23: 'h',
    0x24: 'j', 0x25: 'k', 0x26: 'l', 0x27: 'm', 0x28: 'ù', 0x29: '*', 0x2B: '<', 0x2C: 'w', 0x2D: 'x', 0x2E: 'c',
    0x2F: 'v', 0x30: 'b', 0x31: 'n', 0x32: ',', 0x33: ';', 0x34: ':', 0x35: '!', 0x1C: '\n', 0x39: ' ', 0x0E: 'backspace'
}

# Mapping of key codes to characters with shift
SHIFT_KEY_MAP = {
    0x02: '1', 0x03: '2', 0x04: '3', 0x05: '4', 0x06: '5', 0x07: '6', 0x08: '7', 0x09: '8', 0x0A: '9', 0x0B: '0',
    0x0C: '°', 0x0D: '+', 0x10: 'A', 0x11: 'Z', 0x12: 'E', 0x13: 'R', 0x14: 'T', 0x15: 'Y', 0x16: 'U', 0x17: 'I',
    0x18: 'O', 0x19: 'P', 0x1A: '¨', 0x1B: '£', 0x1E: 'Q', 0x1F: 'S', 0x20: 'D', 0x21: 'F', 0x22: 'G', 0x23: 'H',
    0x24: 'J', 0x25: 'K', 0x26: 'L', 0x27: 'M', 0x28: '%', 0x29: 'µ', 0x2B: '>', 0x2C: 'W', 0x2D: 'X', 0x2E: 'C',
    0x2F: 'V', 0x30: 'B', 0x31: 'N', 0x32: '?', 0x33: '.', 0x34: '/', 0x35: '§', 0x1C: '\n', 0x39: ' ', 0x0E: 'backspace'
}

def parse_keylogger_output(file_path):
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(24)
            if len(chunk) < 24:
                break
            seconds, microseconds, ev_type, code, value = struct.unpack('llHHI', chunk)
            if ev_type == 1 and value == 1:  # EV_KEY and key press event
                yield code

def translate_key_events(key_events):
    typed_text = []
    shift_active = False

    for code in key_events:
        if code in (0x2A, 0x36):  # Left Shift and Right Shift scancodes
            shift_active = True
        elif code == 0x0E:  # Backspace
            if typed_text:
                typed_text.pop()
        else:
            if shift_active:
                typed_text.append(SHIFT_KEY_MAP.get(code, ''))
                shift_active = False
            else:
                typed_text.append(KEY_MAP.get(code, ''))

    return ''.join(typed_text)

def main():
    key_events = list(parse_keylogger_output('keylogger'))
    typed_text = translate_key_events(key_events)
    with open('keylogger_output.txt', 'w') as f:
        f.write(typed_text)
    print("Typed Text:", typed_text)

if __name__ == "__main__":
    main()