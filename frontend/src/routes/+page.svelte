<script>
    let list1 = '';
  let list2 = '';
  let mergedList = [];

  async function mergeLists() {
    const response = await fetch('http://127.0.0.1:8000/merge/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        list1: list1.split(',').map(Number),
        list2: list2.split(',').map(Number),
      }),
    });

    if (response.ok) {
      mergedList = await response.json();
    } else {
      mergedList = ['Error: Unable to merge lists'];
    }
  }
</script>


<main>
    <h1 class="text-4xl font-bold">Merge Two Linked Lists Sorted</h1>

    <div class="form-field mt-4">
        <label for="list1" class="text-md font-semibold">List 1:</label>
        <input  id="list1" bind:value={list1} placeholder="Enter comma separated numbers" class="input input-border w-full max-w-xs"/>
    </div>
    <div class="form-field mt-4">
        <label for="list2" class="text-md font-semibold">List 2:</label>
        <input  id="list2" bind:value={list2} placeholder="Enter comma separated numbers" class="input input-border w-full max-w-xs"/>
    </div>
    

    <button on:click={mergeLists} class="btn btn-primary mt-4">Merge Lists</button>

    <div class="mt-4">
        <h2 class="text-3xl font-sans">Result: </h2>
    </div>
    
    <div class="bg-base-100 p-4 mt-4">
        <pre class="rounded-md p-4 text-accent">{mergedList}</pre>
    </div>
    
    
</main>