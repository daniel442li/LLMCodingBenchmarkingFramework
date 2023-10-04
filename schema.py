main_schema = {
    "type": "object",
    "properties": {
        "identifier": {
            "type": "string",
            "description": "A unique string identifier for the problem. Example: 'problem_2'"
        },
        "description": {
            "type": "string",
            "description": "A brief textual description of the problem or task. Example: 'Write a function to subtract two numbers.'"
        },
        "function_prototype": {
            "type": "object",
            "description": "Information about the expected function solution prototype.",
            "properties": {
                "function_name": {
                    "type": "string",
                    "description": "The expected name of the function to be implemented. Example: 'subtract'"
                },
                "parameters": {
                    "type": "array",
                    "description": "An array detailing the expected parameters for the function.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The name of the parameter. Example: 'a'"
                            },
                            "type": {
                                "type": "string",
                                "description": "The expected type of the parameter. Example: 'int'"
                            }
                        },
                        "required": ["name", "type"]
                    }
                },
                "return_values": {
                    "type": "array",
                    "description": "An array detailing the expected return values of the function.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "description": "The expected type of the return value. Example: 'int'"
                            }
                        },
                        "required": ["type"]
                    }
                }
            },
            "required": ["function_name", "parameters", "return_values"]
        },
        "tags": {
            "type": "array",
            "description": "An array of strings, each string being a tag relevant to the problem. Example: ['Arithmetic', 'Easy']",
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["identifier", "description", "function_prototype", "correctness_test_suite", "tags"]
}

test_case_schema = {
    "type": "object",
    "description": "A schema defining unit test cases for a specific problem. These are input parameters and expected output values.",
    "properties": {
        "correctness_test_suite": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    
                "input": {
                "description": "The input data, an object which can contain various properties of different data types.",
                "type": "object",
                "properties": {
                    "var": {
                        "type": ["object", "array", "string", "number", "boolean", "null"],
                        "description": "An example key; extend the object as per requirements."
                        }
                    }
                },
                    "expected_output": {
                        "description": "The expected output data, which can be of any type.",
                        "type": "array",
                        "items": {
                            "type": ["object", "array", "string", "number", "boolean", "null"]
                        }
                    }
                },
                "required": ["input", "expected_output"]
            }
        }
    },
    "required": ["correctness_test_suite"]
}

prompt_schema = {
    "type": "object",
    "properties": {
        "prompts": {
            "type": "array",
            "description": "An array of prompt objects, each detailing a different context or framing of the problem.",
            "items": {
                "type": "object",
                "properties": {
                    "prompt_id": {
                        "type": "string",
                        "description": "A unique identifier for the prompt."
                    },
                    "prompt": {
                        "type": "string",
                        "description": "A textual instruction or question that describes the task to be accomplished or solved."
                    },
                    "genericize": {
                        "type": "boolean",
                        "description": "A flag indicating whether the prompt is generic."
                    },
                    "sample_inputs_outputs": {
                        "type": "array",
                        "description": "An array of sample input objects and their corresponding expected output.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "input": {
                                "description": "The input data, an object which can contain various properties of different data types.",
                                "type": "object",
                                "properties": {
                                    "var": {
                                        "type": ["object", "array", "string", "number", "boolean", "null"],
                                        "description": "An example key; extend the object as per requirements."
                                        }
                                    }
                                },
                                "expected_output": {
                                    "description": "The expected output data, which can be of any type.",
                                    "type": ["object", "array", "string", "number", "boolean", "null"]
                                }
                            },
                            "required": ["input", "expected_output"]
                        }
                    }
                },
                "required": ["prompt_id", "prompt", "genericize", "sample_inputs_outputs"]
            }
        }
    },
    "required": ["prompts"]
}
