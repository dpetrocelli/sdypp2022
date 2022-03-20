package com.example.demo.dto;

import java.util.List;

public class ProductsResponse {

    private List<ProductDto> products;

    public ProductsResponse(List<ProductDto> products) {
        this.products = products;
    }

    public List<ProductDto> getProducts() {
        return products;
    }
}
