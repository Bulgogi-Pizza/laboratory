package com.cdi.laboratory.laboratory;

import java.util.Collections;
import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LaboratoryController {

    private int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    @GetMapping("/")
    public Map<String, String> hello() {
        return Collections.singletonMap("message", "Hello, World!");
    }

    @GetMapping("/calculate/{number}")
    public Map<String, Object> calculateFib(@PathVariable int number) {
        int result = fibonacci(number);
        return Map.of("number", number, "fibonacci", result);
    }
}

