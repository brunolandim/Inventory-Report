from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Marreta Biônoca",
        nome_da_empresa="Chapolin",
        data_de_fabricacao="13/01/2000",
        data_de_validade="13/01/2022",
        numero_de_serie="131506",
        instrucoes_de_armazenamento="Manter longe do Thanos",
    )

    assert product.id is int
    assert product.nome_do_produto is str
    assert product.nome_da_empresa is str
    assert product.data_de_fabricacao is str
    assert product.data_de_validade is str
    assert product.numero_de_serie is str
    assert product.instrucoes_de_armazenamento is str

