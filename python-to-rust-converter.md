Let's look at how to implement different algorithms and functions in Python vs Rust.

#Iterate alternatively over the elements of the list items1 and items2. For each iteration, print the element.

##Python
```
for pair in zip(item1, item2): print(pair)
```

#Rust
```
extern crate itertools;
for pair in izip!(&items1, &items2) {
    println!("{}", pair.0);
    println!("{}", pair.1);
}
```

# Send a value to another thread

##Python
```
from threading import Thread
from threading import Queue
q = Queue()

t = Thread(target=worker)
t.daemon = True
t.start()

q.put("Alan")
q.put("Turing")
```

##Rust
```
use std::sync::mpsc::channel;
use std::thread;

let (send, recv) = channel();
thread::spawn(move || {
    let msg = recv.recv();
    println!("{}", msg.unwrap());
});

send.send("Alan");
send.send("Turing");
```

#Load JSON file into a string

##Python
```
import json
with open('data.json') as f:
    x = json.load(f)
```

##Rust
```
use std::fs::File;
use serde_json;
let x = ::serde_json::from_reader(File::open("data.json")?)?;
```

#Create an object called Levenshtein with two static methods: ratio and distance.

##Python
```
import numpy as np

class Levenshtein(object):

    @staticmethod
    def __ratio(distance, str_length):
        return 1 - float(distance) / float(str_length)

    @staticmethod
    def ratio(seq1, seq2):
        str_distance = Levenshtein.distance(seq1,seq2)
        str_length = max(len(seq1),len(seq2))
        return Levenshtein.__ratio(str_distance,str_length)

    @staticmethod
    def distance(seq1, seq2):  
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
        matrix = np.zeros ((size_x, size_y))
        for x in range(size_x):
            matrix [x, 0] = x
        for y in range(size_y):
            matrix [0, y] = y

        for x in range(1, size_x):
            for y in range(1, size_y):
                if seq1[x-1] == seq2[y-1]:
                    matrix [x,y] = min(
                        matrix[x-1, y] + 1,
                        matrix[x-1, y-1],
                        matrix[x, y-1] + 1
                    )
                else:
                    matrix [x,y] = min(
                        matrix[x-1,y] + 1,
                        matrix[x-1,y-1] + 1,
                        matrix[x,y-1] + 1
                    )
        return (matrix[size_x - 1, size_y - 1])
```

##Rust
```
use std::cmp::min;
use std::collections::HashMap;

struct Levenshtein {
    cache: HashMap<(String, String), usize>,
}

impl Levenshtein {
    fn new() -> Levenshtein {
        Levenshtein {
            cache: HashMap::new(),
        }
    }

    fn distance(&mut self, seq1: &str, seq2: &str) -> u32 {
        let key = (seq1.to_string(), seq2.to_string());
        if let Some(distance) = self.cache.get(&key) {
            return *distance;
        }
        let mut dp = vec![0; seq1.len()];
        for i in 0..seq1.len() {
            dp[i] = i;
        }
        for i in 1..seq1.len() {
            for j in 1..seq2.len() {
                let cost = if seq1[i] == seq2[j] { 0 } else { 1 };
                dp[j] = min(
                    min(dp[j - 1] + 1, dp[j] + 1),
                    dp[j - 1] + cost
                );
            }
        }
        let distance = dp[seq2.len() - 1];
        self.cache.insert(key, distance);
        distance
    }

    fn _ratio(&mut self, distance: u32, str_length: u32) -> f32 {
        1.0 - (distance as f32 / str_length as f32)
    }

    pub fn ratio(&mut self, seq1: &str, seq2: &str) -> f32 {
        let str_distance = self.distance(seq1, seq2);
        let str_length = max(seq1.len(), seq2.len());
        self.cache.insert((seq1.to_string(), seq2.to_string()), str_distance as u32);
        self._ratio(str_distance, str_length as u32)
    }
}
```

#Type your prompt here
