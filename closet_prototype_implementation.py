'''
Closet = {
        
         "[image link]" : {
                    "Item" : "purse"
                    "color" : "pink"
                    "brand" : unknown
                    

         }
         "[image link]" : {
                    "Item" : "t-shirt"
                    "color" : "white"
                    
         }
}

tags_closet = {
        "purse" : (item, item, item)
        "t-shirt": (item, item, item)

}
'''


def add_to_closet(closet, tags_closet, item_type, color, image_link, brand=None):
    closet[image_link]["Item"] = item_type
    closet[image_link]["Color"] = color
    closet[image_link]["Brand"] = brand
    args = [item_type, color, brand]
    for arg in args:
        if arg not in tags_closet:
            tags_closet[arg] = set(image_link)
        else:
            tags_closet[arg].add(image_link)


def remove_from_closet():
    pass

# tags = ["purse", "pink", "louis vutton"], given these tags find image (image links) with these tags (as a list)
def hard_search_closet(tags_closet, tags):
    hard_matches = []
    # image is the link of the image 
    compare = set()
    i = 0
    while i < len(tags) and tags[i] not in tags_closet:
        i += 1
    intersect_tags = tags_closet[tags[i]]
    while i + 1 < len(tags):
        if tags[i+1] in tags_closet:
            intersect_tags = intersect_tags & tags_closet[tags[i+1]]
        else:
            return None
        i += 1
     # for image in closet:
    #     is_match = True
    #     for i in tags:
    #         if i not in closet[image]:
    #             is_match = False
    #             break
    #     if (is_match):
    #         hard_matches.append(image)
    # return hard_matches
    return list(intersect_tags)
    
   

def soft_search_closet(tags_closet, tags):
    pass





# creates a comparison between objects to create a natural ordering between them
# returns > 0 if image_link_a has more matches with the tags than image_link_b
def compareTo(closet, image_link_a, image_link_b, tags):
    tally_a = 0
    tally_b = 0
    for i in tags:
        if i in closet[image_link_a]: 
            tally_a += 1
        if i in closet[image_link_b]:
            tally_b += 1
    return tally_a - tally_b


tags_manual = ['Purse','Backpack', 'Bag', 'Watch','T-Shirt', 'Dress', 'Pants', 'Bathing Suit' ]
def generate_tags():
    html = ''
    for i in tags_manual:
        html += '<div id="tag" onclick="clickTags()">'
        html += i
        html += '</div>\n'
    return html
print(generate_tags())
    