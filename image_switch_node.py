import torch

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
        
        # If still no image found, create a default black image
        if selected_image is None:
            # Create a default 512x512 black image
            selected_image = torch.zeros((1, 512, 512, 3), dtype=torch.float32)
        
        return (selected_image,)


# Node registration
NODE_CLASS_MAPPINGS = {
    "ImageSwitchNode": ImageSwitchNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageSwitchNode": "Image Switch"
}
