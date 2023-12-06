package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.service.NameService;

import java.util.*;

@RestController
@RequestMapping("/names")
public class NameController {
    private final NameService nameService;

    @Autowired
    public NameController(NameService nameService) {
        this.nameService = nameService;
    }

    @GetMapping
    public List<String> getNames() {
        return nameService.getNames();
    }

    @PostMapping
    public void addName(@RequestBody String name) {
        nameService.addName(name);
    }
}

package com.example.demo.service;


import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class NameService {

    private static List<String> names = new ArrayList<>();

    public List<String> getNames() {
        return names;
    }
    public void addName(String name) {
        names.add(name);
    }

}



