import numpy as np


def embed_data(img, data, method, key_seed=None):

    img_flat = img.flatten()

    binary_data = (
        "".join(format(ord(i), "08b") for i in data)
        + "1111111111111110"
    )

    if len(binary_data) > len(img_flat):
        return None, "Image capacity exceeded!"

    indices = np.arange(len(img_flat))

    if method == "Random LSB":

        if not key_seed:
            return None, "Random LSB password required!"

        seed_val = sum(ord(c) for c in key_seed)

        np.random.seed(seed_val)
        np.random.shuffle(indices)

    for i, bit in enumerate(binary_data):

        target_idx = indices[i]

        img_flat[target_idx] = (
            img_flat[target_idx] & 0xFE
        ) | int(bit)

    return img_flat.reshape(img.shape), None


def extract_data(img, method, key_seed=None):

    img_flat = img.flatten()

    indices = np.arange(len(img_flat))

    if method == "Random LSB":

        if not key_seed:
            return "Password required!"

        seed_val = sum(ord(c) for c in key_seed)

        np.random.seed(seed_val)
        np.random.shuffle(indices)

    bin_str = ""

    for idx in indices:

        bin_str += str(img_flat[idx] & 1)

        if bin_str.endswith("1111111111111110"):
            break

    bin_str = bin_str[:-16]

    try:
        extracted = "".join(
            chr(int(bin_str[i:i+8], 2))
            for i in range(0, len(bin_str), 8)
        )

        return extracted

    except:
        return "Extraction failed!"