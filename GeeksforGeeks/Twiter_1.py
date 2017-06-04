#from collections import defaultdict

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    print(followGraph_edges)
    print(likeGraph_edges)
    follow_dict = {}
    #follow_dict = defaultdict(list)
    #like_dict = defaultdict(list)
    for i in range(len(followGraph_edges)):
        print(followGraph_edges[i][0])
        follow_dict.setdefault(followGraph_edges[i][0], [])
        follow_dict[followGraph_edges[i][0]].append(followGraph_edges[i][1])
    like_dict = {}
    for i in range (len(likeGraph_edges)):
        print(likeGraph_edges[i][0])
        like_dict.setdefault(likeGraph_edges[i][0], [])
        like_dict[likeGraph_edges[i][0]].append(likeGraph_edges[i][1])

    get_follow = []

    get_follow = follow_dict.get(targetUser)
    print(get_follow)

    if (get_follow != None):
        tweet_dict = {}
        tweet = []
        for i in range(len(get_follow)):
            tweet.append(like_dict.get(get_follow[i]))
        fintweet = sum(tweet, [])

        for i in range(len(fintweet)):
            count = tweet_dict.get(fintweet[i])
            if (count == None):
                count = 1
            else:
                count += 1
            tweet_dict[fintweet[i]] = count
    result = []
    print(tweet_dict)
    #print(sorted(tweet_dict.items(), key=lambda x: x[1]))
    for k in tweet_dict:
        print(tweet_dict[k])
        if tweet_dict[k] >= minLikeThreshold:
            result.append([k,tweet_dict[k]])
        # if (int(v) >= minLikeThreshold):
        #     result.append(k)
    finres = []
    for k,v in (sorted(result, key=lambda x: x[1])):
        finres.append(k)
    # print(result.sort(key=lambda x: x[1]))
    # print(result.sort())
    print(finres)

from collections import defaultdict
followGraph_edges = [['A','B'],['A','C'],['A','D'],['A','E'],['B','C'],['B','D']]
likeGraph_edges = [['B','T1'],['B','T2'],['B','T3'],['C','T1'],['C','T2'],['D','T3'],['D','T4'],['E','T1'],['E','T2'],['E','T3']]
targetUser = 'A'
minLikeThreshold = 2
getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold)
