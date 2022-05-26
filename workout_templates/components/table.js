class ThreeSetTable extends HTMLElement {
    constructor() {
      super();
    }
  
  connectedCallback() {
    this.innerHTML = `
      <style>

      .exercise_name {
        display: grid;
        place-items: center;
      }

      table.GeneratedTable {
        width: 100%;
        background-color: #ffffff;
        border-collapse: collapse;
        border-width: 2px;
        border-color: #002fff;
        border-style: solid;
        color: #000000;
      }

      table.GeneratedTable td,
      table.GeneratedTable th {
        border-width: 1px;
        border-color: #003cff;
        border-style: solid;
        padding: 3px;
      }

      table.GeneratedTable thead {
        background-color: #009dff;
      }

      </style>

        <h2 class="exercise_name">${this.getAttribute('exercise')}</h2>
        <table class="GeneratedTable">
          <thead>
            <tr>
              <th>set no</th>
              <th>reps</th>
              <th>weight / kg</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="exercise_name"><strong>1</strong></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td class="exercise_name"><strong>2</strong></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td class="exercise_name"><strong>3</strong></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
    `;
  }
}

class TwoSetTable extends HTMLElement {
    constructor() {
      super();
    }
  
  connectedCallback() {
    this.innerHTML = `
      <style>

      .exercise_name {
        display: grid;
        place-items: center;
      }

      table.GeneratedTable {
        width: 100%;
        background-color: #ffffff;
        border-collapse: collapse;
        border-width: 2px;
        border-color: #002fff;
        border-style: solid;
        color: #000000;
      }

      table.GeneratedTable td,
      table.GeneratedTable th {
        border-width: 1px;
        border-color: #003cff;
        border-style: solid;
        padding: 3px;
      }

      table.GeneratedTable thead {
        background-color: #009dff;
      }

      </style>

        <h2 class="exercise_name">${this.getAttribute('exercise')}</h2>
        <table class="GeneratedTable">
          <thead>
            <tr>
              <th>set no</th>
              <th>reps</th>
              <th>weight / kg</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="exercise_name"><strong>1</strong></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td class="exercise_name"><strong>2</strong></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>
    `;
  }
}

customElements.define('three-set-table-component', ThreeSetTable);
customElements.define('two-set-table-component', TwoSetTable);
