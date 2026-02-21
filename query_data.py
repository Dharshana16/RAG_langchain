import argparse
from retrieval import retrieve_context
from llm_handler import generate_answer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str)
    args = parser.parse_args()

    query_text = args.query_text

    # Step 1: Retrieve relevant context
    context, results = retrieve_context(query_text)

    if not results:
        print("No relevant documents found.")
        return

    # Step 2: Generate answer using LLM
    answer = generate_answer(context, query_text)

    print("\n============================")
    print("Final Answer")
    print("============================\n")
    print(answer)

if __name__ == "__main__":
    main()