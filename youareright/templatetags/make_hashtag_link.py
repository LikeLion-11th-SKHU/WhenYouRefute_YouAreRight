from django import template

register = template.Library()


@register.filter
def hashtag_link(word):
    content = word.content
    hashtags = word.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(
            hashtag.content, f'<a href="/youareright/{hashtag.pk}/hashtag/">{hashtag.content}</a> ')
    return content


@register.filter
def hashtag_links(word):
    content = word.content
    hashtags = word
    content = content.replace(hashtags.content, f'<a href="/youareright/{hashtags.pk}/hashtag/">{hashtags.content}</a> ')
    return content
