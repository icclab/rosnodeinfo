# rosnodeinfo

ROS node that publishes to a topic all of the currently running nodes. By default the name of the published topic is `running_nodes` and the node name is `nodeInfoPublisher`.

```
rosrun rosnodeinfo nodes.py
```

For a different topic name and/or node name

```
rosrun rosnodeinfo nodes.py _topic:='example_topic_name' __name:='example_node_name'
```


