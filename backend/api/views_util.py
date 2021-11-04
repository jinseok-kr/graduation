def obj_to_post(obj):
    post = dict(vars(obj))

    if obj.modify_dt:
        post['modify_dt'] = obj.modify_dt.strftime('%Y-%m-%d %H:%M')
    else:
        post['modify_dt'] = ''

    if obj.tags:
        post['tags'] = [tag.name for tag in obj.tags.all()]
    else:
        post['tags'] = []

    if obj.owner:
        post['owner'] = obj.owner.username
    else:
        post['owner'] = 'Anonymous'

    del post['_state']

    return post


def prev_next_post(obj):
    try:
        prevObj = obj.get_prev()
        prevDict = {'id': prevObj.id, 'title': prevObj.title}
    except obj.DoesNotExist as e:
        prevDict = {}

    try:
        nextObj = obj.get_next()
        nextDict = {'id': nextObj.id, 'title': nextObj.title}
    except obj.DoesNotExist as e:
        nextDict = {}

    return prevDict, nextDict


def make_tag_cloud(qsTag):
    if not qsTag:
        return []
    minCount = min(tag.count for tag in qsTag)
    maxCount = max(tag.count for tag in qsTag)

    # minweight, maxweight = 1, 3
    def get_weight_func(minweight, maxweight):
        if minCount == maxCount:
            factor = 1.0
        else:
            factor = (maxweight - minweight) / (maxCount - minCount)

        factor = (maxweight - minweight) / (maxCount - minCount)

        def func(count):
            weight = (minweight + (factor * (count - minCount)))
            return weight

        return func

    weight_func = get_weight_func(1, 3)

    tagList = []
    for tag in qsTag:
        weight = weight_func(tag.count)
        tagList.append({
            'name': tag.name,
            'count': tag.count,
            'weight': weight,
        })

    if len(tagList) > 30:
        return tagList[:30]
    else:
        return tagList

### NEWS API UTIL
def obj_to_news(obj):
    news = dict(vars(obj))

    if obj.create_date:
        news['create_date'] = obj.create_date.strftime('%Y-%m-%d %H:%M')
    else:
        news['create_date'] = ''

    if obj.keywords:
        news['keywords'] = [keyword.name for keyword in obj.keywords.all()]
    else:
        news['keywords'] = []

    del news['_state']

    return news
