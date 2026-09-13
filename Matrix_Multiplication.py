import random
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
SIZE = 100

A = []
B = []
C = []

threads = []
animation_data = []

lock = threading.Lock()
completed_cells = 0


A = [
    [random.randint(1, 10) for _ in range(SIZE)]
    for _ in range(SIZE)
]

B = [
    [random.randint(1, 10) for _ in range(SIZE)]
    for _ in range(SIZE)
]

C = [
    [0 for _ in range(SIZE)]
    for _ in range(SIZE)
]


def calculate_cell(i, j):

    global completed_cells

    total = 0

    for k in range(SIZE):

        multiplication = A[i][k] * B[k][j]

        total += multiplication

    
    C[i][j] = total

    
    with lock:

        completed_cells += 1

        thread_name = threading.current_thread().name

        
        if (
            completed_cells == 1
            or completed_cells % 100 == 0
            or completed_cells == SIZE * SIZE
        ):

            animation_data.append({
                "row": i,
                "column": j,
                "thread": thread_name,
                "completed": completed_cells,
                "matrix": [row[:] for row in C]
            })

for i in range(SIZE):

    for j in range(SIZE):

        thread = threading.Thread(
            target=calculate_cell,
            args=(i, j)
        )

        threads.append(thread)

        thread.start()



for thread in threads:
    thread.join()

print("MATRIX MULTIPLICATION")


print("Size of the matrix      :", SIZE, "x", SIZE)
print("Total number of result cells:", SIZE * SIZE)
print("Threads used in multiplication      :", len(threads))
print(
    "Total number of multiplications:",
    SIZE * SIZE * SIZE
)

print("\nMatrix multiplication completed.")



fig, axes = plt.subplots(
    1,
    3,
    figsize=(15, 5)
)

fig.patch.set_facecolor("black")

for ax in axes:
    ax.set_facecolor("black")



axes[0].imshow(A)
axes[0].set_title(
    "Matrix A (100 × 100)",
    color="white"
)



axes[1].imshow(B)
axes[1].set_title(
    "Matrix B (100 × 100)",
    color="white"
)



result_image = axes[2].imshow(
    animation_data[0]["matrix"]
)

axes[2].set_title(
    "Result Matrix C (100 × 100)",
    color="white"
)


for ax in axes:

    ax.tick_params(
        colors="white"
    )

    for spine in ax.spines.values():
        spine.set_color("white")



def update(frame):

    data = animation_data[frame]

    row = data["row"]
    column = data["column"]

    thread_name = data["thread"]

    completed = data["completed"]

    current_matrix = data["matrix"]


    result_image.set_data(current_matrix)

    for ax in axes:

        for line in ax.lines:
            line.remove()


  
    axes[2].plot(
        column,
        row,
        marker="s",
        markersize=12,
        markerfacecolor="none",
        markeredgewidth=2
    )

    percentage = (
        completed / (SIZE * SIZE)
    ) * 100


    fig.suptitle(
        "THREADED MATRIX MULTIPLICATION",
        color="white",
        fontsize=18,
        fontweight="bold"
    )


    axes[2].set_xlabel(
        f"C[{row}][{column}]"
        f"\nThread: {thread_name}"
        f"\nProgress: {completed}/{SIZE * SIZE}"
        f" ({percentage:.2f}%)",
        color="white"
    )


    return result_image,



animation = FuncAnimation(
    fig,
    update,
    frames=len(animation_data),
    interval=100,
    repeat=False
)


animation.save(
    "matrix_multiplication.gif",
    writer=PillowWriter(fps=10)
)


plt.close()


print("\nAnimation saved as: matrix_multiplication.gif")