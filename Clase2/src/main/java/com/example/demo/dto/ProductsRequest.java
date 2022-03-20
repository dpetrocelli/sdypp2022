package com.example.demo.dto;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Positive;
import java.math.BigDecimal;

public class ProductsRequest {

    @NotNull(message = "Name can't be null")
    @NotBlank
    @Pattern(regexp = "[a-zA-Z]+", message = "Name must be alphabetical")
    private String name;

    @Positive(message = "Price must be > 0")
    private BigDecimal price;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "ProductsRequest{" +
                "name='" + name + '\'' +
                ", price=" + price +
                '}';
    }
}
