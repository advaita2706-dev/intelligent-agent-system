# Intelligent Agent System

Hey! This is my AI/ML project for the Fundamentals course. Spent quite a bit of time figuring out how agents actually work and got to implement some cool search algorithms + ML models.

## What's This Project About?

Basically I wanted to build something that shows how intelligent agents work in practice. The idea was to create agents that can look at their surroundings, figure out what to do, and then actually do it - kind of like how we learned in class about the perceive-decide-act cycle.

I also added search algorithms (A* was tricky to get right!) and some machine learning classifiers because I thought it'd be interesting to see how these different AI concepts work together.

## Main Features

So there are basically 3 main parts:

### 1. Agent Stuff
- Made a base agent class that other agents can inherit from
- Agents can sense their environment 
- They decide what action to take
- Then execute that action
- Also tracks how well they're performing

### 2. Search Algorithms  
- **A* Search** - This one took me forever to debug lol. Finally got it working with proper heuristics
- **Greedy Best-First** - Simpler than A* but doesn't always find optimal solution
- Both keep track of nodes expanded and stuff for analysis

### 3. ML Models
- KNN Classifier - k=5 worked best for my tests
- Decision Trees - pretty straightforward implementation
- Can train, predict, and check accuracy

## Tech I Used

- Python (obviously)
- numpy & pandas for data stuff
- scikit-learn (for the ML parts, didn't wanna reinvent the wheel)
- matplotlib for some graphs
- pytest for testing (tried to cover the main functions at least)

## Folder Structure

Here's how I organized everything:

```
intelligent-agent-system/
├── src/
│   ├── agents/          # Agent classes
│   ├── search/          # Search algorithms  
│   ├── ml_models/       # ML stuff
│   └── utils/           # Helper functions
├── tests/               # Unit tests
├── data/                # Sample datasets
├── examples/            # Demo scripts
├── requirements.txt
├── README.md
└── statement.md
```

## How to Run This

### Setup
First clone it:
```bash
git clone https://github.com/advaita2706-dev/intelligent-agent-system.git
cd intelligent-agent-system
```

Make a virtual environment (recommended!):
```bash
python -m venv venv
venv\Scripts\activate  # on Windows
# source venv/bin/activate  # on Mac/Linux
```

Install requirements:
```bash
pip install -r requirements.txt
```

### Running Examples

Using the agent:
```python
from src.agents.rational_agent import RationalAgent
from src.search.informed_search import AStarSearch

# create an agent
agent = RationalAgent(name="Agent-01")

# define your problem 
problem = agent.define_problem(start_state, goal_state)

# solve it with A*
search = AStarSearch(heuristic_function)
solution = search.search(initial_state, goal_test, get_successors)

print(f"Path found: {solution}")
```

ML example:
```python
from src.ml_models.classifier import KNNClassifier
from src.data_processing.preprocessor import DataPreprocessor

# prep the data
preprocessor = DataPreprocessor()
X_train, X_test, y_train, y_test = preprocessor.prepare_data('data/sample_data.csv')

# train model
knn = KNNClassifier(k=5)
knn.train(X_train, y_train)

# check accuracy
acc = knn.evaluate(X_test, y_test)
print(f"Got {acc}% accuracy")
```

## Testing

Run tests with:
```bash
pytest tests/
```

I covered most of the main functions but there's probably room for more edge case tests.

## Requirements Met

Just to checklist the project requirements:

**Functional Requirements:**
- [x] 3 major modules (agents, search, ML)
- [x] Clear input/output
- [x] Logical workflow

**Non-functional:**
- [x] Performance - search completes in reasonable time
- [x] Usability - tried to keep code readable with comments
- [x] Reliability - added error handling where needed
- [x] Maintainability - modular design, PEP 8 style
- [x] Testing - unit tests included

## Challenges I Faced

1. **A* Implementation** - Getting the heuristic function right was harder than I thought. Had to debug why it wasn't finding optimal paths.

2. **Agent Design** - Struggled initially with making the base class abstract enough but still useful.

3. **Testing** - Writing good unit tests is harder than writing the code itself sometimes!

4. **Time Management** - Balancing this with other coursework was tough.

## What I Learned

- How agent architectures actually work in practice (not just theory)
- Implementing search algorithms from scratch gives you way better understanding  
- Scikit-learn makes ML implementation much easier
- Good documentation really helps when you come back to code later
- Testing is important (saved me from some bugs)

## Future Improvements

If I had more time I'd add:
- More search algorithms (maybe IDA*)
- Better visualization of agent behavior
- More ML models (neural nets?)
- Performance optimizations
- Better test coverage

## Notes

This project was for my AI/ML course at VIT Bhopal. The code is public so feel free to check it out but please don't just copy it for your own projects - actually learn from it!

All the main concepts are from our course lectures plus the AIMA textbook (Russell & Norvig).

## Contact

Advaita  
VIT Bhopal  
GitHub: @advaita2706-dev

---

**Repository**: https://github.com/advaita2706-dev/intelligent-agent-system

Last updated: November 2025
