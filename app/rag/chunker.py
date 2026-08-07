class TextChunker:

    def __init__(
        self,
        chunk_size=800,
        overlap=100
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, documents):

        chunks = []

        for document in documents:

         sections = document["content"].split("\n## ")

         for i, section in enumerate(sections):

                if i == 0:
                      content = section
                else:
                     content = "## " + section

                section_title = "Introduction"

                lines = content.split("\n")

                if lines:

                    first_line = lines[0].strip()

                    if first_line.startswith("#"):
                        section_title = first_line.replace("#", "").strip()

                chunks.append({

                    "chunk_id": len(chunks),

                     "path": document["path"],

                     "topic": document["path"].split("\\")[-1].replace(".md", ""),

                    "section": section_title,

                     "content": content

                })
        return chunks