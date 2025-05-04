import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image

def analyze_bouquet_image(prompt) -> str:
	vertexai.init(project='qwiklabs-gcp-03-5b0ab703f306', location='us-east4',)
	multimodal_model = GenerativeModel("gemini-2.0-flash-001")
	response = multimodal_model.generate_content(
	[
	Part.from_image(Image.load_from_file("image.jpeg")
	),
	prompt,
	]
	)
	return response.text


response = analyze_bouquet_image("Generate birthday wishes based on this image?")
print(response)

