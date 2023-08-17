from django import template

register = template.Library()


@register.filter
def hashtag_link(word):
    content = word.body
    hashtags = word.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(
            hashtag.content, f'<a style="text-decoration: none; color: #434343;" href="/{hashtag.pk}/hashtag/">{hashtag.content}</a> ')
    return content


@register.filter
def hashtag_links(word):
    content = word.content
    hashtags = word
    content = content.replace(hashtags.content, f'<a class="hashtag-link" href="/{hashtags.pk}/hashtag/"><div class="popular-hashtag">{hashtags.content}</div></a> ')
    return content
