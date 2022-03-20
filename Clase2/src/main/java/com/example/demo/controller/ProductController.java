package com.example.demo.controller;

import com.example.demo.dto.ProductDto;
import com.example.demo.dto.ProductsRequest;
import com.example.demo.dto.ProductsResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.validation.FieldError;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping(path = "/products")
public class ProductController {

    Logger logger = LoggerFactory.getLogger(ProductController.class);

    @GetMapping
    public ProductsResponse getProducts(@RequestParam(required = false) String name, @RequestParam(required = false) BigDecimal price) {
        logger.info(name);
        ProductDto product = new ProductDto(name, price);
        return new ProductsResponse(List.of(product));
    }

    @GetMapping(path = "/{product_id}")
    public ProductsResponse getProductById(@PathVariable(name = "product_id") String id) {
        logger.info("{}", id);
        return new ProductsResponse(Arrays.asList(new ProductDto(id, "Random product")));
    }


    @PostMapping
    public ProductsResponse saveProduct(@RequestBody @Valid ProductsRequest request) {
        logger.info("{}", request);
        return new ProductsResponse(List.of(new ProductDto(request.getName(), request.getPrice())));
    }

    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public Map<String, String> handleValidationExceptions(
            MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getAllErrors().forEach((error) -> {
            String fieldName = ((FieldError) error).getField();
            String errorMessage = error.getDefaultMessage();
            errors.put(fieldName, errorMessage);
        });
        return errors;
    }


}