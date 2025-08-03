import torch
from typing import Any, Tuple

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

WILDCARD = AnyType("*")

class SwitchAnyValid:
    """
    A switch node that takes up to 4 optional inputs of any type.
    Selects the first input that is not None.
    Throws an exception if more than one input is provided (not None).
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "input_1": (WILDCARD, {"tooltip": "First optional input"}),
                "input_2": (WILDCARD, {"tooltip": "Second optional input"}),
                "input_3": (WILDCARD, {"tooltip": "Third optional input"}),
                "input_4": (WILDCARD, {"tooltip": "Fourth optional input"}),
            }
        }
    
    RETURN_TYPES = (WILDCARD,)
    RETURN_NAMES = ("output",)
    FUNCTION = "switch_valid"
    CATEGORY = "utils/switch"
    
    def switch_valid(self, input_1: Any = None, input_2: Any = None, input_3: Any = None, input_4: Any = None) -> Tuple[Any]:
        """
        Selects the first non-None input. Throws an exception if more than one input is provided.
        
        Args:
            input_1: First optional input
            input_2: Second optional input
            input_3: Third optional input
            input_4: Fourth optional input
            
        Returns:
            Tuple containing the selected input
            
        Raises:
            ValueError: If more than one input is not None
        """
        inputs = [input_1, input_2, input_3, input_4]
        non_none_inputs = [inp for inp in inputs if inp is not None]
        
        if len(non_none_inputs) == 0:
            return (None,)
        elif len(non_none_inputs) == 1:
            return (non_none_inputs[0],)
        else:
            raise ValueError(f"SwitchAnyValid: Expected exactly one input, but received {len(non_none_inputs)} inputs")

class ImageSwitchNode:
    """
    A ComfyUI node that allows selecting one image from up to 8 input image sources.
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "select": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 8,
                    "step": 1,
                    "display": "number"
                }),
            },
            "optional": {
                "image_1": ("IMAGE",),
                "image_2": ("IMAGE",),
                "image_3": ("IMAGE",),
                "image_4": ("IMAGE",),
                "image_5": ("IMAGE",),
                "image_6": ("IMAGE",),
                "image_7": ("IMAGE",),
                "image_8": ("IMAGE",),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "switch_image"
    CATEGORY = "image/switch"
    
    def switch_image(self, select, **kwargs):
        """
        Switches between the input images based on the select parameter.
        
        Args:
            select (int): The index of the image to select (1-8)
            **kwargs: The optional image inputs (image_1 through image_8)
            
        Returns:
            tuple: A tuple containing the selected image
        """
        # Map select value to image key
        image_key = f"image_{select}"
        
        # Get the selected image from kwargs
        selected_image = kwargs.get(image_key)
        
        # If the selected image is None, try to find the first available image
        if selected_image is None:
            for i in range(1, 9):
                fallback_key = f"image_{i}"
                if fallback_key in kwargs and kwargs[fallback_key] is not None:
                    selected_image = kwargs[fallback_key]
                    break
        
        return (selected_image,)


# Node registration
NODE_CLASS_MAPPINGS = {
    "ImageSwitchNode": ImageSwitchNode,
    "SwitchAnyValid": SwitchAnyValid
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageSwitchNode": "Image Switch",
    "SwitchAnyValid": "Switch Any Valid"
}
