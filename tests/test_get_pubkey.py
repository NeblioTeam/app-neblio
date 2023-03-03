from bitcoin_client.bitcoin_base_cmd import AddrType


def test_get_public_key(cmd):
    # legacy address
    pub_key, addr, bip32_chain_code = cmd.get_public_key(
        addr_type=AddrType.Legacy,
        bip32_path="m/44'/146'/0'/0/0",
        display=False
    )

    assert pub_key == bytes.fromhex("04"
                                    "7162aa5a07cf0cbf9b58f025d2f4966d94f3150d05bce1257fc46fad5ffb2ec5"
                                    "b8b1de5093fb42ff7dd607ad4dea9cdb097b7b68839aab0faa3b2debbc80b07a")
    assert addr == "NXaKcB9qDSEX3PJwDsVFW8pdoqVq45rimT"
    assert bip32_chain_code == bytes.fromhex("9d1d55a9d34a61f1bf7533fc648905034dfd3887cfd8221c42b3d80064cd02de")

    # P2SH-P2WPKH address
    pub_key, addr, bip32_chain_code = cmd.get_public_key(
        addr_type=AddrType.P2SH_P2WPKH,
        bip32_path="m/49'/146'/0'/0/0",
        display=False
    )

    assert pub_key == bytes.fromhex("04"
                                    "e9cca04bd9fb18bc165d6ce534cca49fdf881aa4634fc792f5bdd57b13eac674"
                                    "279b0bb9f966509bbba2ead8fdd58bb8ce0f77079b0bcf954460f7e0c1933833")
    assert addr == "n9op2DdptVYz8R8smKComaEn3PYm7K8PdH"
    assert bip32_chain_code == bytes.fromhex("68dc4924d16ffeee070424452d19cebeddb682ac2af5bd41d0a0e97ce9370ec5")

    # bech32 address
    pub_key, addr, bip32_chain_code = cmd.get_public_key(
        addr_type=AddrType.BECH32,
        bip32_path="m/84'/1'/0'/0/0",
        display=False
    )

    assert pub_key == bytes.fromhex("04"
                                    "7cb75d34b005c4eb9f62bbf2c457d7638e813e757efcec8fa68677d950b63662"
                                    "648e4f638cabc4e4383fa3fe8348456e46fa56742dcf500a5b50dc1d403492f0")
    assert addr == "bc1qzdr7s2sr0dwmkwx033r4nujzk86u0cy6rae6f9"
    assert bip32_chain_code == bytes.fromhex("efd851020a3827ba0d3fd4375910f0ed55dbe8c5d740b37559e993b1d623a956")
