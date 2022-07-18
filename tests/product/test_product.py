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

    assert product.id == 1
    assert product.nome_do_produto == "Marreta Biônoca"
    assert product.nome_da_empresa == "Chapolin"
    assert product.data_de_fabricacao == "13/01/2000"
    assert product.data_de_validade == "13/01/2022"
    assert product.numero_de_serie == "131506"
    assert product.instrucoes_de_armazenamento == "Manter longe do Thanos"
