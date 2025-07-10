from PIL import Image
import torch
import clip
import numpy as np

# Load CLIP model once globally
clip_model, preprocess = clip.load("ViT-B/32")

def rank_tags_with_clip(image: Image.Image, candidate_tags: list):
    if not candidate_tags:
        return []
    
    image_input = preprocess(image).unsqueeze(0)
    text_inputs = torch.cat([clip.tokenize(f"a photo of {tag}") for tag in candidate_tags])

    with torch.no_grad():
        image_features = clip_model.encode_image(image_input)
        text_features = clip_model.encode_text(text_inputs)

        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        similarity = (100.0 * image_features @ text_features.T).squeeze()
        
        if len(candidate_tags) == 1:
            ranked_tags = [(candidate_tags[0], round(similarity.item(), 2))]
        else:
            
            k = min(5, len(candidate_tags))
            values, indices = similarity.topk(k)
            
       
            if k == 1:
                values = values.unsqueeze(0)
                indices = indices.unsqueeze(0)
            
            ranked_tags = [(candidate_tags[indices[j].item()], round(values[j].item(), 2)) for j in range(k)]
        
    return ranked_tags