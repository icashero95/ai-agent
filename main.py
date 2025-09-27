import sys
from generate_content import generate_content
from messages import init_messages


def main():
    if len(sys.argv) < 2:
        print("No prompt arguments provided.")
        sys.exit(1)
    
    print("Hello from ai-agent!")
    user_prompt = sys.argv[1]
    messages = init_messages(user_prompt)
    verbose = (len(sys.argv) > 2) and (sys.argv[2] == "--verbose")

    max_iters = 20
    for i in range(max_iters):
        try:
            response = generate_content(messages, verbose=verbose)
        except Exception as e:
            print(f"Error on iteration {i+1}: {e}")
            break


        if getattr(response, "function_calls", None):
            continue

        # If the model produced final text, print and stop
        if getattr(response, "text", None):
            print("Final response:")
            print(response.text)
            break
    else:
        if verbose:
            print("Reached max iterations without final text.")
    
    
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
