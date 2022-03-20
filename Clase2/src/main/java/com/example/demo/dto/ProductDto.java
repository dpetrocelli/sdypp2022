package com.example.demo.dto;

import com.fasterxml.jackson.annotation.JsonInclude;

import java.math.BigDecimal;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class ProductDto {

    private String id;

    private String description;

    private BigDecimal price;

    public ProductDto(String description, BigDecimal price) {
        this.description = description;
        this.price = price;
    }

    public ProductDto(String id, String name) {
        this.id = id;
        this.description = name;
    }

    public String getId() {
        return id;
    }

    public String getDescription() {
        return description;
    }

    public BigDecimal getPrice() {
        return price;
    }
}
