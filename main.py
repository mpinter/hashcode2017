videos = {}
endpoints = {}
caches = {}
requests = {}

init = input().split()
numVideos = int(init[0]) #TODO
numEndpoints = int(init[1])
numRequests = int(init[2])
numCaches = int(init[3])
cacheSize = int(init[4])

# video = {'id', 'size', requests: {ednpointId: {id, num}} }
# endpoint = {id, latency, caches: {id: {id, latency}}}
# caches = {id, endpoints: {id, latency}}
# requests = {requests, video, endpoint}

for i in range(numVideos):
    videos[i] = {
        'id': i,
        'requests': dict(),
    }
for i in range(numEndpoints):
    endpoints[i] = {
        'id': i,
        'caches': dict(),
    }
for i in range(numCaches):
    caches[i] = {
        'id': i,
        'endpoints': dict(),
    }
for i in range(numRequests):
    requests[i] = {
        'id': i,
        'endpoints': dict(),
    }

#read sizes
sizes = [int(i) for i in input().split()]
videoIdCounter = 0
for s in sizes:
    videos[videoIdCounter]['size'] = s
    videoIdCounter+=1
for e in range(numEndpoints):
    eLine = [int(i) for i in input().split()]
    endpoints[e]['latency'] = eLine[0]
    for c in range(eLine[1]):
        cLine = [int(i) for i in input().split()]
        endpoints[e]['caches'][cLine[0]] = {
            'id': cLine[0],
            'latency': cLine[1],
        }
        caches[cLine[0]]['endpoints'][e] = {
            'id': e,
            'latency': cLine[1],
        }

for r in range(numRequests):
    rLine = [int(i) for i in input().split()]
    requests[r] = {
        'requests': rLine[2],
        'videoId': rLine[0],
        'endpointId': rLine[1],
    }
    videos[rLine[0]]['requests'][rLine[1]] = {
        'id': rLine[1],
        'num': rLine[2],
    }

  
print(caches)
