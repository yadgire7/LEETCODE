# trip_to_location_mapper = {}
# for tid, lid in zip(trips['trip_id'], trips['location_id']):
#     trip_to_location_mapper[tid] = lid

# # Order id to issue id counter
# order_id_to_issues = {}
# for oid, iid in zip(order_issues_joined[order_id], order_issues_joined[issue_id]):
#     if oid not in order_id_to_issues.keys():
#         order_id_to_issues[oid] = 1
#     else:
#         order_id_to_issues[oid] += 1


# trip_id_to_details_map = {}
# for tid, oid, tm in zip(trip_order_joined['trip_id'], trip_order_joined['order_id'], trip_order_joined['total_miles']):
#     if tid not in trip_id_to_details_map.keys():
#         trip_id_to_details_map[tid] = {
#             'orders':[(oid, tm)],
#             'issues': 0
#         }
#         if oid in order_id_to_issues.keys():
#             trip_id_to_details_map[tid]['issues'] += order_id_to_issues[oid]
#     else:
#         trip_id_to_details_map[tid]['orders'] = trip_id_to_details_map[tid]['orders'].append(oid, tm)

my_dict ={'orders':[(1,2.1),(2,3.2)]}
sum = 0
for o in my_dict['orders']:
    sum +=o[1]
print(sum)