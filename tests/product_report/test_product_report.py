from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Marreta Biônoca",
        nome_da_empresa="Chapolin",
        data_de_fabricacao="13/01/2000",
        data_de_validade="13/01/2022",
        numero_de_serie="131506",
        instrucoes_de_armazenamento="Manter longe do Thanos",
    )

    assert str(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
