class WriteComment:
    def write_comment(self):
        # Code de la fonction write_comment
        pass

def process_comments(write_comment_instance):
    # Appel de la méthode write_comment de l'instance de WriteComment
    write_comment_instance.write_comment()


# Définir la fonction pour écrire un commentaire _________________________________________________

def write_comment(filename):
    comment_text = f"New page added from {filename}"
    comment_element = ET.Comment(comment_text)
    body.append(comment_element)
    return comment_element